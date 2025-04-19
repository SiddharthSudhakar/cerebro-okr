// Frontend React App for OKR/KPI Tracker

import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Card, CardContent } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Select, SelectItem } from '@/components/ui/select';

export default function App() {
  const [goals, setGoals] = useState([]);
  const [selectedGoal, setSelectedGoal] = useState('');
  const [keyResults, setKeyResults] = useState([]);
  const [employees, setEmployees] = useState([]);
  const [allocations, setAllocations] = useState([]);
  const [kpis, setKpis] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/goals').then((res) => setGoals(res.data));
    axios.get('http://localhost:8000/api/employees').then((res) => setEmployees(res.data));
    axios.get('http://localhost:8000/api/allocations').then((res) => setAllocations(res.data));
    axios.get('http://localhost:8000/api/kpis').then((res) => setKpis(res.data));
  }, []);

  useEffect(() => {
    if (selectedGoal) {
      axios.get(`http://localhost:8000/api/key-results?objective_id=${selectedGoal}`).then((res) => setKeyResults(res.data));
    }
  }, [selectedGoal]);

  return (
    <div className="p-6 grid gap-6 max-w-5xl mx-auto">
      <Card>
        <CardContent>
          <h2 className="text-2xl font-bold mb-4">Select Organizational Goal</h2>
          <Select onValueChange={(val) => setSelectedGoal(val)}>
            {goals.map((goal) => (
              <SelectItem key={goal.objective_id} value={goal.objective_id}>
                {goal.objective_name}
              </SelectItem>
            ))}
          </Select>
        </CardContent>
      </Card>

      {keyResults.length > 0 && (
        <Card>
          <CardContent>
            <h3 className="text-xl font-semibold mb-2">Key Results</h3>
            <ul className="list-disc list-inside">
              {keyResults.map((kr) => (
                <li key={kr.key_result_id}>
                  {kr.key_result_name} — Target: {kr.target_figure}
                </li>
              ))}
            </ul>
          </CardContent>
        </Card>
      )}

      <Card>
        <CardContent>
          <h3 className="text-xl font-semibold mb-2">Employee Directory</h3>
          <ul className="space-y-2">
            {employees.map((emp) => (
              <li key={emp.employee_id}>{emp.employee_name}</li>
            ))}
          </ul>
        </CardContent>
      </Card>

      <Card>
        <CardContent>
          <h3 className="text-xl font-semibold mb-2">Project Allocations</h3>
          <ul className="space-y-2">
            {allocations.map((alloc) => (
              <li key={alloc.allocation_id}>
                Employee: {alloc.employee_id} → Project: {alloc.project_id} ({alloc.allocation_percent}%)
              </li>
            ))}
          </ul>
        </CardContent>
      </Card>

      <Card>
        <CardContent>
          <h3 className="text-xl font-semibold mb-2">KPI Tracker</h3>
          <ul className="space-y-2">
            {kpis.map((kpi) => (
              <li key={kpi.tracker_id}>
                Emp: {kpi.employee_id} | KR: {kpi.key_result_id} → {kpi.actual_value} ({kpi.status})
              </li>
            ))}
          </ul>
        </CardContent>
      </Card>
    </div>
  );
}
