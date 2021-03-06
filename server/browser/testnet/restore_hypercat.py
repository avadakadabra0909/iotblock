from iotblock_sdk.pathfinder import Catalogue
import iotblock_sdk.hypercat as hypercat
import json
import logging
TEST_PATHFINDER_URL_ROOT = "http://127.0.0.1:8888/cat"

def unittest():
    
    
    print("Running tests")
    logging.getLogger().setLevel(logging.DEBUG)

    print("Create a catalogue on Pathfinder")
    p = Catalogue(TEST_PATHFINDER_URL_ROOT, "Vkc5clpXNGdZWEJwWDJ0bGVUMGlPR1EzT0dKaE0yWTRaV1l3TWpCak5XUTROamsxWXpKak56ZGlObVk1Tkdaall6RTFaR1U0TnpOaFlUVmpOVGd6WmpaaE5XUm1NMk5qTWpJd09UVmtNeUlnWVhWMGFEMGlNSGhHWWpNek5EZzVZak5DUmpkRU1ERmtOMk5FTmtNNFEwSkZRMEk1TkRSbE5EZEJPRFprT0dKa0lpQmxkR2hmWTI5dWRISnBZajBpTVRBd01EQXdNREF3TURBd01EQWk6")
    h1 = hypercat.Hypercat("Dummy test catalogue")
    print(h1);
    with open('backups/1.json') as json_data:
        data = json.load(json_data)
    #p.backup('backups/1.json');
    
    h1 = hypercat.loads(json.dumps(data))
    print(json.dumps(h1.asJSON(), indent=4))
    p.create(h1)
    print("Read it")
    h2 = hypercat.loads(json.dumps(p.get()))

    print("Did we get back what we wrote?")
    print("h1:")
    print(h1.asJSON())
    print("h2:")
    print(h2.asJSON())
    assert(h1.asJSON() == h2.asJSON())

    print("All tests passed")
    
if __name__ == '__main__':
    # Unit tests
    unittest()
