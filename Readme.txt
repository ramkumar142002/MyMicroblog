Setting up elasticsearch

Navigate to installed elasticsearch folder in terminal as administrator

1.Get the token:
bin\elasticsearch-create-enrollment-token -s node

2.Setup config using token:
bin\elasticsearch --enrollment-token <token>

3.Get the default password for user:
bin\elasticsearch-reset-password -u elastic

4.Check the elastic search is running:
& "C:\Windows\System32\curl.exe" --cacert "C:\Program Files\elasticsearch-8.17.0\config\certs\http_ca.crt" --ssl-no-revoke -u elastic:<password>+o https://localhost:9200


5.Starting elasticsearch server:
.\bin\elasticsearch

6. navigate to http(s)://localhost:9200 to verify if the elastic search server is started.
