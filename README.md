# LearningFactory

## Setting Up a Local Development Environment
### Prerequisites
Before you can set up a local development environment for this project, you'll need to install the following software on your computer:
* Python 3.7 or later (for the HTTP request)
* Any compatible Python IDE (Spyder, VSCode, etc.)
* PostgreSQL 9.6 or later (for the database to store machine data)
* DBeaver Community Edition (for managing the database)
* Ignition Designer by Inductive Automation (for viewing the Ignition dashboard)

### Setting Up the Database
To set up the database for the project, follow these steps:
1. Create a new database connection in DBeaver. Select PostgreSQL as the database software and use the credentials specified during the PostgreSQL install to make the connection. Credentials include host, port, database name, username, and password. 
2. Now connected, create a new PostgreSQL database on your local computer using DBeaver. 
3. Run the SQL script included in the project's GitHub repository to create tables for each machine you want to monitor. 

### Running the Python Script
To run the Python script that makes an HTTP request to the server receiving machine data, follow these steps:
1. Clone the project's repository to your local machine.
2. Using the Python IDE, install the required Python packages specified at the top of each script.
3. Set the server-specific variables shown below the Python packages within each Python script. Those variables include the server URL (including IP address), API parameters, and any authentication credentials for the server and database connection.
4. Run the Python script within the IDE.

### Viewing the Ignition Dashboard
To view the Ignition dashboard, follow these steps:
1. Open the Ignition Designer application.
2. After specifying the designer, import the dashboard project by selecting `LearningFactoryWIP_2023-04-12_1549` zip file.
3. Run the project by selecting `Project > Start Project` in the Ignition Designer.
4. Observe any change in machine variables indicated by the dashboard alert table, control chart, or other components.

### Conclusion
That's it! With these instructions, you should be able to set up a local development environment, run the Python script, and view the Ignition dashboard containing machine data from Virginia Tech’s Learning Factory, a Northrop Grumman facility, or any other manufacturing facility aiming to advance its digital transformation.
