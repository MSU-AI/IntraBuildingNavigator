from floor_plan import FloorPlan, Node, Edge, Room, Portal


def main():
    eb = engineering_building_first_floor()
    print(eb)

    test = test_floor_plan()
    print(test)

def test_floor_plan() -> FloorPlan:
    test_floor_plan = FloorPlan("test")

    test_floor_plan.add_node("Room 1100")
    test_floor_plan.add_room("Room 1103")
    test_floor_plan.add_room("Room 1105")
    test_floor_plan.add_room("Room 1107")

    test_floor_plan.add_edges_by_node_name(
        "Room 1100", 
        [
            test_floor_plan.get_node_by_name("Room 1100"), 
            test_floor_plan.get_node_by_name("Room 1103")
        ]
    )

    return test_floor_plan

def engineering_building_first_floor() -> FloorPlan:
    eb_floor_1 = FloorPlan("Engineering Building")

    # 11xx rooms
    eb_floor_1.add_room("Room 1100")
    eb_floor_1.add_room("Room 1103")
    eb_floor_1.add_room("Room 1105")
    eb_floor_1.add_room("Room 1107")
    eb_floor_1.add_room("Room 1108")
    eb_floor_1.add_room("Room 1109")
    eb_floor_1.add_room("Room 1120")
    eb_floor_1.add_room("Room 1118")
    eb_floor_1.add_room("Room 1124")
    eb_floor_1.add_room("Room 1126")
    eb_floor_1.add_room("Room 1128")
    eb_floor_1.add_room("Room 1129")
    eb_floor_1.add_room("Room 1133")
    eb_floor_1.add_room("Room 1135")
    eb_floor_1.add_room("Room 1138")
    eb_floor_1.add_room("Room 1140")
    eb_floor_1.add_room("Room 1130")
    eb_floor_1.add_room("Room 1145")
    eb_floor_1.add_room("Room 1148")
    eb_floor_1.add_room("Room 1160")

    # 12xx rooms
    eb_floor_1.add_room("Room 1200")
    eb_floor_1.add_room("Room 1202")
    eb_floor_1.add_room("Room 1204")
    eb_floor_1.add_room("Room 1206")
    eb_floor_1.add_room("Room 1208")
    eb_floor_1.add_room("Room 1210")
    eb_floor_1.add_room("Room 1211")
    eb_floor_1.add_room("Room 1213")
    eb_floor_1.add_room("Room 1215")
    eb_floor_1.add_room("Room 1216")
    eb_floor_1.add_room("Room 1217")
    eb_floor_1.add_room("Room 1218")
    eb_floor_1.add_room("Room 1219")
    eb_floor_1.add_room("Room 1220")
    eb_floor_1.add_room("Room 1225")
    eb_floor_1.add_room("Room 1226")
    eb_floor_1.add_room("Room 1228")
    eb_floor_1.add_room("Room 1232")
    eb_floor_1.add_room("Room 1230")
    eb_floor_1.add_room("Room 1233")
    eb_floor_1.add_room("Room 1234")
    eb_floor_1.add_room("Room 1237")
    eb_floor_1.add_room("Room 1239")
    eb_floor_1.add_room("Room 1240")
    eb_floor_1.add_room("Room 1243")
    eb_floor_1.add_room("Room 1245")
    eb_floor_1.add_room("Room 1248")
    eb_floor_1.add_room("Room 1252")
    eb_floor_1.add_room("Room 1254")
    eb_floor_1.add_room("Room 1255")
    eb_floor_1.add_room("Room 1257")
    eb_floor_1.add_room("Room 1258")
    eb_floor_1.add_room("Room 1259")
    eb_floor_1.add_room("Room 1261")
    eb_floor_1.add_room("Room 1262")
    eb_floor_1.add_room("Room 1260")
    eb_floor_1.add_room("Room 1270")
    eb_floor_1.add_room("Room 1271")
    eb_floor_1.add_room("Room 1273")
    eb_floor_1.add_room("Room 1274")

    # 13xx rooms
    eb_floor_1.add_room("Room 1300")
    eb_floor_1.add_room("Room 1303")
    eb_floor_1.add_room("Room 1306")
    eb_floor_1.add_room("Room 1307")
    eb_floor_1.add_room("Room 1312")
    eb_floor_1.add_room("Room 1318")
    eb_floor_1.add_room("Room 1320")
    eb_floor_1.add_room("Room 1328")
    eb_floor_1.add_room("Room 1325")
    eb_floor_1.add_room("Room 1342")
    eb_floor_1.add_room("Room 1338")
    eb_floor_1.add_room("Room 1340")
    eb_floor_1.add_room("Room 1345")

    # 14xx rooms
    eb_floor_1.add_room("Room 1408")
    eb_floor_1.add_room("Room 1410")
    eb_floor_1.add_room("Room 1415")
    eb_floor_1.add_room("Room 1416")
    eb_floor_1.add_room("Room 1420")
    eb_floor_1.add_room("Room 1422")
    eb_floor_1.add_room("Room 1424")
    eb_floor_1.add_room("Room 1426")
    eb_floor_1.add_room("Room 1428")

    # 15xx rooms
    eb_floor_1.add_room("Room 1500")
    eb_floor_1.add_room("Room 1501")
    eb_floor_1.add_room("Room 1502")
    eb_floor_1.add_room("Room 1503")
    eb_floor_1.add_consecutive_rooms(1508, 1516)
    eb_floor_1.add_room("Room 1520")
    eb_floor_1.add_room("Room 1522")
    eb_floor_1.add_room("Room 1526")
    eb_floor_1.add_room("Room 1528")
    eb_floor_1.add_room("Room 1530")
    eb_floor_1.add_room("Room 1531")
    eb_floor_1.add_room("Room 1532")
    eb_floor_1.add_room("Room 1535")
    eb_floor_1.add_room("Room 1538")
    eb_floor_1.add_room("Room 1540")

    return eb_floor_1

if __name__ == '__main__':
    main()
