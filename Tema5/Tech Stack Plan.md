## Backend Server Platform

### Core stack

- Hardware/VM host: AWS Cloud Services
- Operating System: Windows
- Data store: AWS Cloud Services
- Application Framework: Express for NodeJS
- Application Server: Windows Server 
- Web Server: NodeJS server
- Scheduling: None
- Logging: AWS Cloud and in-server locally stored
- API: NodeJS

### Communication

- API paradigm: REST
- Data format: JSON
- Availability monitoring: AWS Cloud Monitoring

### Data

- Data Storage : MongoDB based storage

### Documentation

- For the WebAPI : Github stored docs according to OpenAPI (Swagger) specifications
- For development purposes : Github stored .md files containing 
- For users/customers : In-app built tutorials, hints and helpers 

### Core stack

- Monthly server budget : maximum 500$/month first 3 months
- Expected user load : 3000 - 5000 users first 3 months
- Failover requirements : Required only for the API Server, any other instance will be cloud-hosted
- Single VM based server and storage, only for the initial business plan

### Security

- Transport encryption: HTTPS and TLS client-server communication
- Authentication: JWT based authentication
- Data encryption: Locally stored data encrypted through the Android platform

## TODO/Unknowns to determine