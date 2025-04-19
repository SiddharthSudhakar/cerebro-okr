# Database Schema and details

# 📊 Organizational Goals and Employee Management Schema

This schema defines the structure for managing organizational goals, key results, employee data, and project assignments. It includes tables for hierarchical relationships and master reference data to maintain consistency and scalability.

---

## 🏆 Organizational Goals

### **Table: `OrganizationalGoals`**
| Column         | Type         | Description                     |
|----------------|--------------|---------------------------------|
| `ObjectiveID`  | Primary Key  | Unique ID for each objective    |
| `ObjectiveName`| Text         | Name of the objective           |

---

## 🎯 Organizational Key Results

### **Table: `OrganizationalKeyResults`**
| Column         | Type         | Description                                         |
|----------------|--------------|-----------------------------------------------------|
| `KeyResultID`  | Primary Key  | Unique ID for each key result                      |
| `ObjectiveID`  | Foreign Key  | References `OrganizationalGoals.ObjectiveID`       |
| `KeyResultName`| Text         | Name of the key result                             |
| `MetricUnits`  | Text         | Unit of measurement (e.g., %, $, hrs)              |
| `MetricFigures`| Numeric      | Quantitative value for the metric                  |
| `DepartmentID` | Foreign Key  | References `MasterDepartments.DepartmentID`        |
| `GroupID`      | Foreign Key  | References `MasterGroups.GroupID`                 |
| `RoleID`       | Foreign Key  | References `MasterRoles.RoleID`                    |
| `TargetID`     | Text/Int     | Target identifier (optional context-specific)      |

---

## 👥 Employees

### **Table: `Employees`**
| Column              | Type         | Description                                           |
|---------------------|--------------|-------------------------------------------------------|
| `EmployeeID`        | Primary Key  | Unique ID for each employee                           |
| `EmployeeName`      | Text         | Full name of the employee                             |
| `GroupID`           | Foreign Key  | References `MasterGroups.GroupID`                     |
| `DepartmentID`      | Foreign Key  | References `MasterDepartments.DepartmentID`           |
| `RoleID`            | Foreign Key  | References `MasterRoles.RoleID`                       |
| `LevelID`           | Foreign Key  | References `MasterLevels.LevelID`                     |
| `ReportingManagerID`| Foreign Key  | Self-referencing `EmployeeID` for reporting structure |

---

## 📋 Project Allocation List

### **Table: `ProjectAllocationList`**
| Column             | Type         | Description                                  |
|--------------------|--------------|----------------------------------------------|
| `EmployeeID`       | Foreign Key  | References `Employees.EmployeeID`            |
| `PrimaryProjectID` → `FifteenthProjectID` | Foreign Keys | Each references `MasterProjects.ProjectID` (up to 15 slots) |

---

## 📏 Master Metric Units

### **Table: `MasterMetricUnits`**
| Column     | Type        | Description              |
|------------|-------------|--------------------------|
| `MetricID` | Primary Key | Unique ID for metric     |
| `MetricName` | Text      | Name of the metric unit  |

---

## 🏢 Master Tables

### **Table: `MasterGroups`**
| Column     | Type        | Description              |
|------------|-------------|--------------------------|
| `GroupID`  | Primary Key | Unique group identifier  |
| `GroupName`| Text        | Name of the group        |

### **Table: `MasterDepartments`**
| Column        | Type        | Description                |
|---------------|-------------|----------------------------|
| `DepartmentID`| Primary Key | Unique department ID       |
| `DepartmentName`| Text      | Name of the department     |

### **Table: `MasterProjects`**
| Column     | Type        | Description              |
|------------|-------------|--------------------------|
| `ProjectID`| Primary Key | Unique project identifier |
| `ProjectName`| Text      | Name of the project       |

### **Table: `MasterLevels`**
| Column   | Type        | Description               |
|----------|-------------|---------------------------|
| `LevelID`| Primary Key | Unique level identifier   |
| `LevelName`| Text      | Name of the level         |

### **Table: `MasterRoles`**
| Column   | Type        | Description              |
|----------|-------------|--------------------------|
| `RoleID` | Primary Key | Unique role identifier   |
| `RoleName`| Text       | Name of the role         |

---

## 🔗 Key Relationships

- **OrganizationalKeyResults** links to:
  - `OrganizationalGoals` via `ObjectiveID`
  - `MasterDepartments` via `DepartmentID`
  - `MasterGroups` via `GroupID`
  - `MasterRoles` via `RoleID`

- **Employees** links to:
  - `MasterGroups` via `GroupID`
  - `MasterDepartments` via `DepartmentID`
  - `MasterRoles` via `RoleID`
  - `MasterLevels` via `LevelID`
  - Self via `ReportingManagerID`

- **ProjectAllocationList** links to:
  - `Employees` via `EmployeeID`
  - `MasterProjects` via project columns (`PrimaryProjectID` to `FifteenthProjectID`)



# RAW

Organizational Goals
Objective ID: Primary Key
Objective Name
Organizational Key Results
Objective ID: Foreign Key to Organizational Goals
Key Result ID: Primary Key
Key Result Name
Metric Units
Metric Figures
Department ID: Foreign Key to Master Table Department
Group ID: Foreign Key to Master Table Group
Role ID: Foreign Key to Master Role
TargetID
Employees
Employee ID: Primary Key
Employee Name
Group ID: Foreign Key to Master Table Group
Department ID: Foreign Key to Master Table Department
Role ID: Foreign Key to Master Role
Level ID: Foreign Key to Master Level
Reporting Manager ID: Self-referential Foreign Key to Employee ID
Project Allocation List
Employee ID: Foreign Key to Employees
Primary Project ID: Foreign Key to Master Projects
Second Project ID: Foreign Key to Master Projects
Third Project ID: Foreign Key to Master Projects
Fourth Project ID: Foreign Key to Master Projects
Fifth Project ID: Foreign Key to Master Projects
Sixth Project ID: Foreign Key to Master Projects
Seventh Project ID: Foreign Key to Master Projects
Eighth Project ID: Foreign Key to Master Projects
Ninth Project ID: Foreign Key to Master Projects
Tenth Project ID: Foreign Key to Master Projects
Eleventh Project ID: Foreign Key to Master Projects
Twelfth Project ID: Foreign Key to Master Projects
Thirteenth Project ID: Foreign Key to Master Projects
Fourteenth Project ID: Foreign Key to Master Projects
Fifteenth Project ID: Foreign Key to Master Projects
Master Metric Units
Metric ID: Primary Key
Metric Name
Master Table Group
Group ID: Primary Key
Group Name
Master Table Department
Department ID: Primary Key
Department Name
Master Projects
Project ID: Primary Key
Project Name
Master Level
Level ID: Primary Key
Level Name
Master Role
Role ID: Primary Key
Role Name
Key Relationships
Organizational Key Results links to Organizational Goals, Master Table Department, Master Table Group, and Master Role.
Employees links to Master Table Group, Master Table Department, Master Role, and Master Level.
Project Allocation List links to Employees and Master Projects.