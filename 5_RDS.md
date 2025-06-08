# Amazon RDS
This service is for managing relational databases easily and efficiently

## Good to Know
- Template : for practice should select free tier
- Storage autoscaling : can select max storage threshold
- Should create RDS-VPC-SG for security
- Database Auth : Should save the username and password for login
- Enable auto minor version upgrade in Maintenance **Disable it to make it not auto upgrade db 
- mysql -h <rds-endpoint> -u <username> -p : access mysql db