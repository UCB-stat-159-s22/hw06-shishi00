import json
from ligotools import readligo as rl

def test_loaddata():
    fnjson = "data/BBH_events_v3.json"
    events = json.load(open(fnjson,"r")) 
    eventname = 'GW150914' 
    event = events[eventname]
    fn_H1 = event['fn_H1'] 
    
    strain_H1, time_H1, chan_dict_H1 = rl.loaddata('data/' + fn_H1, 'H1')
    assert len(strain_H1) == 131072

