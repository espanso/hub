# US Time Zones

This package converts current time to US time zones.

## Installation

```
espanso install us-time-zones
```

## Usage

The triggers are based on timezone and hour-format desired. Daylight savings is based system timezone and is printed with output. 

#### Examples

`:et12` for Eastern Time, 12-Hour format. 

`:pt24` for Pacific Time, 24-Hour format.



### Eastern Time

**America/New_York - Eastern Standard Time (EST) / Eastern Daylight Time (EDT)**

|  Trigger  | Replacement |
|-----------|---------|
| `:et12`   | 04:31:28 PM EDT |
| `:et24`   | 16:33:51 EDT |

---

### Central Time

**America/Chicago - Central Standard Time (CST) / Central Daylight Time (CDT)**

|  Trigger  | Replacement |
|-----------|---------|
| `:ct12`   | 03:35:13 PM CDT |
| `:ct24`   | 15:35:21 CDT |

---

### Mountain Time

**America/Denver - Mountain Standard Time (MST) / Mountain Daylight Time (MDT)**

|  Trigger  | Replacement |
|-----------|---------|
| `:mt12`   | 02:36:28 PM MDT |
| `:mt24`   | 14:36:35 MDT |

---

### Pacific Time

**America/Los_Angeles - Pacific Standard Time (PST) / Pacific Daylight Time (PDT)**

|  Trigger  | Replacement |
|-----------|---------|
| `:pt12`   | 01:37:54 PM PDT |
| `:pt24`   | 13:38:02 PDT |

---

### Alaska Time

**America/Anchorage - Alaska Standard Time (AKST) / Alaska Daylight Time (AKDT)**

|  Trigger  | Replacement |
|-----------|---------|
| `:at12`   | 12:39:02 PM AKDT |
| `:at24`   | 12:39:09 AKDT |

---

### Hawaii-Aleutian Time

**America/Adak - Hawaii-Aleutian Standard Time (HAST) / Hawaii-Aleutian Daylight Time (HADT)**

|  Trigger  | Replacement |
|-----------|---------|
| `:hat12`   | 11:42:09 AM HDT |
| `:hat24`   | 11:41:25 HDT |

---