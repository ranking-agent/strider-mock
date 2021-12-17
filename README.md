# strider-mock
testing util for mocking sync and async query operations 


# `Seeding` app with data

```
wget -O a0_query.json "https://raw.githubusercontent.com/NCATSTranslator/minihackathons/main/2021-12_demo/workflowA/A.0_RHOBTB2_direct_inverse.json"
wget -O c3_query.json "https://raw.githubusercontent.com/NCATSTranslator/minihackathons/main/2021-12_demo/workflowC/C3.json"


curl -X 'POST' \
  'https://strider.renci.org/1.2/query' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d @a.0_query.json > a.0_RHOBTB2_direct_output.json
  

curl -X 'POST' \
  'https://strider.renci.org/1.2/query' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d @c3_query.json > c3_output.json
 ```
 
 # Running the app
 
 ```
 pip install -r requirements.txt
 python main.py
 ```
 
