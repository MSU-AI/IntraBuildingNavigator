from floor_plan import FloorPlan


def main():
    test_floor_plan = FloorPlan()

    room_1 = FloorPlan.Node("room 1")
    room_2 = FloorPlan.Node("room 2")

    edge_1_to_2 = FloorPlan.Edge(room_1, room_2)

    test_floor_plan.add_node(room_1)
    test_floor_plan.add_node(room_2)

    test_floor_plan.add_edge(edge_1_to_2)
    print()
    print(test_floor_plan._graph)
    print()


if __name__ == '__main__':
    main()
