http://localhost:6789/api/pipeline_schedules/12/pipeline_runs/6dcec89bbe2444eea5703cab0adc263d

curl --location "http://localhost:6789/api/runs" \
--header "Authorization: Bearer 6dcec89bbe2444eea5703cab0adc263d" \
--header "Content-Type: application/json" \
--header "Cookie: lng=en" \
--data "{
    "run": {
        "pipeline_uuid": "predict",
        "block_uuid": "inference",
        "variables":{
            "inputs": [
                {
                    # target = "duration": 11.5
                    'DOLocationID': 239,
                    'PULocationID': 236,
                    'trip_distance': 1.98,
                },
                {
                    # target = "duration" 20.8666666667
                    'DOLocationID': '170',
                    'PULocationID': '65',
                    'trip_distance': 6.54,
                }
            ]
        }
    }
}"