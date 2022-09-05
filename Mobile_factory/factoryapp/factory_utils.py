from random import randint
import json
from weakref import ref

def order_summery(components_list : list):
    """An order will be valid if it contains one, and only one, part of Screen, Camera, Port, OS and Body.
       If an order is valid, the priced order should be calculated
.

    Args:
        param1: components_list : list : Ex ["I","A","D","F","K"]
       

    Returns:
        resullt_dict: dict 
        The return value. {"order_summery":final_result, "is_valid":valid_flag}

    """
    total = 0
    parts_of_list =[]
    final_result = {}
    order_id = randint(100, 999)
    file = open("factory_database.json","r")
    x = file.read()
    reference_data = json.loads(x)
    for component in components_list:
        ref_component = reference_data[component]
        price = ref_component[0]
        part = ref_component[1]
        parts_of_list.append(part)
        total += price
    order_report={"order_id":order_id,"Total":total,"parts":parts_of_list}
    parts_list = order_report["parts"]
    check_list = ["Screen","Camera","Port","OS","Body"]
    valid_flag = True
    parts_count_dict = {"Screen":0,"Camera":0,"Port":0,"OS":0,"Body":0}

    for c_part in check_list:
        for part in parts_list:
            if c_part in part:            
                parts_count_dict[c_part] = parts_count_dict[c_part] + 1
            if parts_count_dict[c_part] >= 2:
                valid_flag = False
                break
        if valid_flag is False:
            break
    result_dict = {"order_summery":order_report, "is_valid":valid_flag}
    return result_dict