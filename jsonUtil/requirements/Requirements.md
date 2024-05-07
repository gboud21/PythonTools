# Requirements Manager Requirements
## Overview
This tool provides the ability to identify data within a strongly formatted data set and extract the data. 
The extracted data can then be used to generate formatted artifacts.

## Template
|Req ID|Requirement Text|
|---|---|
|1|The Requirements Manager shall .|

## High-Level Requirements
### Interfaces
|1|The Requirements Manager shall be executable from the command line using arguments.|
|1|The Requirements Manager shall accept the path to the configuration file as an input argument.|
|1|The Requirements Manager shall use the current directory as the default path to the configuration file.|

### Configuration File
|Req ID|Requirement Text|
|---|---|
|1|The Configuration File shall use the "SystemSpecPath" field to specify the path to the Systems Requirement Specification.|
|1|The Configuration File shall use the "SoftwareSpecPath" field to specify the path to the Software Requirement Specification.|
|1|The Configuration File shall use the "OutputPath" field to specify the path to output the generated Software Requirement Specification and Requirements Update Table to.|
|1|The Configuration File shall use the "RequirementToken" field to specify the pattern used to identify a requirement in the System Requirement Specification.|

## Low-Level Requirements
### Fault Management
|Req ID|Requirement Text|
|---|---|
|1|The Requirements Manager shall classify faults as follows:<br>1. Critical<br>2. Non-Critical|
|1|When a fault is detected, the Requirements Manager shall log a message with the following data:<br>1. System Time<br>2. Fault Description<br>3. Fault Severity<br>4. Corrective Action.|
|1|When a Critical fault is detected, the Requirements Manager shall shutdown.|


### Initialization
|Req ID|Requirement Text|
|---|---|
|1|During initialization, the Requirements Manager shall load the Configuration File.|
|1|If the configuration file does not exist then the Requirements Manager shall generate a Critical fault.|
|1|If the configuration file does not contain the SystemSpecPath field then the Requirements Manager shall generate a Critical fault.|
|1|If the configuration file does not contain the SoftwareSpecPath field then the Requirements Manager shall generate a Critical fault.|
|1|If the configuration file contains a blank SoftwareSpecPath field and the OutputPath is not specified then the Requirements Manager shall generate a Critical fault.|
|1|If the configuration file does not contain the RequirementToken field then the Requirements Manager shall generate a Critical fault.|
|1|The Requirements Manager shall verify all specified file paths exist.|
|1|The Requirements Manager shall verify the Systems Spect Path is readable.|
|1|The Requirements Manager shall verify the Software Spec Path is readable.|
|1|If the Output Path is not specified then the Requirements Manager shall default the output path to the Software Spec Path.|
|1|The Requirements Manager shall verify the Output Path is writeable.|

### Systems Requirement Specification Parsing
|Req ID|Requirement Text|
|---|---|
|1|If the Software Requirements Specification exists then the Requirements Manager shall generate a list of all Systems Requirements traced to by the Software Requirements Specification.|
|1|The Requirements Manager shall search each line in the System Requirement Specification for requirements.|
|1|The Requirements Manager shall use the pattern specified by the RequirementToken field to identify a requirement in the System Requirement Specification .|
|1|The Requirements Manager shall store all requirements identified from the System Requirement Specification for use in the Software Requirements Specifiation generation.|

### System Requirements Report
|Req ID|Requirement Text|
|---|---|
|1|The Requirements Manager shall compare the identified System Requirements, Requirements List A, to the System Requirements identified in the Software Requiremens Trace, Requirements List B.|
|1|The Requirements Manager shall identify all requirements in List A that are not in List B as new.|
|1|The Requirements Manager shall identify all requirements in List A whose ID is equal to the ID in  List B, but whose text is different as updated.|
|1|The Requirements Manager shall identify all requirements in List B that are not in List A as deleted.|
|1|The Requirements Manager shall output the new, updated and deleted requirements table to a file named "SystemsRequirementReport.md" in the directory specified by the OutputPath field.|

### Derived Software Requirements Specification Generation
|Req ID|Requirement Text|
|---|---|
|1|The Requirements Manager shall use the ID specified by each System Requirement with ".md" appeneded as the name for each Derived Software Requirements Specification file. For example if a System Requirement ID is "REQ_1" then the name of the Derived Software Requirements file would be "REQ_1.md"|
|1|The Requirements Manager shall generate a new Derived Software Requirements Specification file for all "new" System Requirements.|