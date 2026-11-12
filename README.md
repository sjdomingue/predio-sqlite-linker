\# Predio-SQLite Linker Plugin (QGIS)



A QGIS plugin prototype that connects spatial parcel layers to an external SQLite database. 

This is a generic portfolio version built with fictitious data to demonstrate database 

integration and PyQGIS skills.



\## Problem



Cross-referencing spatial parcel data in QGIS with tabular records (owners, status, 

debts) stored in external SQLite databases is a manual, error-prone process. 

It typically requires exporting CSVs, doing VLOOKUPs in Excel, and re-importing, 

taking \*\*\~3 hours per dataset\*\*.



\## Solution



A modular plugin architecture that:

\- Connects to a local SQLite database securely.

\- Matches records using a unique ID (e.g., cadastral code).

\- Prepares the data to be displayed as a new attribute table or exported.



\## Result



The workflow is reduced from \*\*\~3 hours to 15 minutes\*\*, eliminating manual 

copy-paste errors and providing a fully reproducible, auditable environment.



\## Demo



!\[Demo](docs/demo.png)



\## Installation (3 steps)



1\. Install QGIS 3.x and clone this repository.

2\. Ensure the sample SQLite database is in the `data/` folder.

3\. Enable the plugin in QGIS: `Plugins → Manage and Install Plugins → Install from ZIP`.



\## Stack



\- Python 3 · PyQGIS (QGIS 3.x API)

\- SQLite3 (Python built-in library)

\- Fictitious test data (included in `data/`)



\## License



MIT — see \[LICENSE](LICENSE).



> Data disclaimer: this repository uses ONLY fictitious/synthetic data. 

> No real cadastral records or corporate data are included.

