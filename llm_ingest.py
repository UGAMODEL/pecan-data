from openai import OpenAI

client = OpenAI()

tools = [
    {
        "type": "function",
        "function": {
            "name": "make_shelling_experiment",
            "description": "This function creates a shelling experiment with defined variables that can later take exerimental data",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "The datetime of the experiment",
                    },
                    "drum-rpm": {
                        "type": "number",
                        "description": "The speed of the drum in RPM",
                    },
                    "paddle-shaft-rpm": {
                        "type": "number",
                        "description": "The speed of the paddle shaft in RPM",
                    },
                    "ring-gap": {
                        "type": "number",
                        "description": "The gap between the drum and the ring in mm",
                    },
                    "tilt-angle": {
                        "type": "number",
                        "description": "The angle of the drum in degrees",
                    },
                    "moisture-content": {
                        "type": "number",
                        "description": "The moisture content of the material in %",
                    },
                    "feed-rate": {
                        "type": "number",
                        "description": "The rate at which material is fed into the drum in kg/h",
                    },
                },
                "required": [
                    "drum-rpm",
                    "paddle-shaft-rpm",
                    "ring-gap",
                    "tilt-angle",
                    "moisture-content",
                ],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "take_measurement",
            "description": "This function takes a measurement of a shelling experiment for a given output parameter",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "The name of the experiment",
                    },
                    "value": {
                        "type": "number",
                        "description": "The measured value",
                    },
                },
                "required": ["name", "value"],
            },
        },
    },
]

prompt = """
Based on the text provided to you by the user, use the provided tools to create a new experiment and ingest the data.
"""

user_prompt = """
7-19-2024 

Meyer Exp.  
0.290 displacement  
6.7% moisture 
0.45 Ring Gap
 

Batch 1 

600 paddle 
35 drum 
Tilt angle 3.5
Input: 33.45
Discharge: 
5.84
Throughput: 17.5%
Final Discharge: 5.22
Output 1: 4.16 | 15.9%
Output 2: 5.80 | 22.1%
Output 3: 16.27 | 62%

Loss %: 5.97%

Half Yield Percentage: 

Output 1: 
50.76
53.70
50.13
54.65
Avg: 52.31%

Output 2: 
54
71.31
62.33
122.29
Avg: 77.48%

Output 3: 
69.43
61.56
67.27
72.82
Avg: 67.77%

Batch - 2 

400 paddle 
35 drum 
Tilt angle 3.5
Input: 32.2
Discharge: 
6.92
6.68
7.28
6.58
6.74
5.82
6
Discharge Throughput: 142.9%
Final Discharge: 5.08
Output 1: 5.86 | 24.2%
Output 2: 5.34 | 22.1%
Output 3: 12.97 | 53.7%

Loss %: 9.2%


Half Yield Percentage: 

Output 1: 
67.67
69
69.71
62.65
Avg: 67.26%

Outpu 2: 
82.88
73.53
82.07
68.48
Avg: 76.74%

Output 3
61.63
70.58
76.61
73.32
Avg: 70.64%
"""

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": user_prompt},
    ],
)

print(response.choices[0].message.content)
