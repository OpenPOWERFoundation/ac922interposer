# ac922interposer

The purpose of this design is to enable the AC922 to accept a DC-SCM v1.0 hardware management module.  This enables a developement
platform for software development.

For connection with a DC-SCM, the DC-SCM v1.0 release design specifies the connector as an SFF-TA-1002 compliant 4C+ connector. The 4C+ connector is a 4C compliant connector with an additional 28-pin “OCP bay” defined in the OCP NIC 3.0 specification.  The right-angled variety allows for the DC-SCM to lay within the BMC cage assembly.  This can be implemented with TE 2336568-1.

References:

DC-SCM 0.95 Draft Specification:
https://www.opencompute.org/documents/ocp-dc-scm-spec-rev-0-95-pdf

DC-SCM 2.0 Draft Specification:
https://drive.google.com/file/d/1UkFgAFKh8qz4mAXdvodYsW0fg8XhyVf2/view?usp=sharing

AC922 Specification:
see OpenPower website

SFF-TA-1002 Protocol Agnostic Multi-Lane High Speed Connector
https://members.snia.org/document/dl/27231

AntMicro Design Specification:
https://github.com/antmicro/artix-dc-scm.git
