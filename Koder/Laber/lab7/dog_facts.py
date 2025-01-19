import json
import requests

def get_dog_facts(json_string):
    # Json til Python dict
    data = json.loads(json_string)
    
    #vil kun hente første faktaen osv.
    #first_fact = data['data'][0]['attributes']['body']
    # Henter faktaen, ikke hardkodet
    facts = [fact['attributes']['body'] for fact in data['data']]
    
    return facts

#henter data og skriver dette ut
def download_dog_facts():
    url = "https://dogapi.dog/api/v2/facts?limit=3"  
    headers = {
        'User-Agent': 'inf100.ii.uib.no abc123', 
    }

    # henter dataen
    response = requests.get(url, headers=headers)

    
    # gjør om til string
    webpage_content = response.content.decode('utf-8')

    # henter fakaten
    facts = get_dog_facts(webpage_content)

    print("Hundefakta:")
    for fact in facts:
        print(f"- {fact}")
    return facts
  
    

def test_get_dog_facts():
    arg = '''\
{
  "data": [
    {
      "id": "574c4504-250f-4743-9ff2-124e5c61e79e",
      "type": "fact",
      "attributes": {
        "body": "Dogs live an average of 15 years."
      }
    },
    {
      "id": "cd131ea1-3327-4c2c-93e6-488582a3e2e7",
      "type": "fact",
      "attributes": {
        "body": "Dogs have a wet nose to help them absorb scents."
      }
    },
    {
      "id": "58d82e49-0b2f-4911-bdde-0d686e092b72",
      "type": "fact",
      "attributes": {
        "body": "Dogs can see in color, but not as vividly as humans."
      }
    }
  ]
}
'''
    expected = [
        'Dogs live an average of 15 years.',
        'Dogs have a wet nose to help them absorb scents.',
        'Dogs can see in color, but not as vividly as humans.',
    ]
    actual = get_dog_facts(arg)
    assert expected == actual


if __name__ == "__main__":
    test_get_dog_facts()
    #henter og skriver ut faktaen
    json_string=download_dog_facts()
    










