import local as vg_local

# vg_local.save_scene_graphs_by_id(data_dir='../data/original/', image_data_dir='../result/scene_graphs/')

# Load scene graphs in 'data/by-id', from index 0 to 200.
# We'll only keep scene graphs with at least 1 relationship.
scene_graphs = vg_local.get_scene_graphs(start_index=0, end_index=-1, min_rels=1, data_dir='../data/original/',
                                         image_data_dir='../../result/scene_graphs/')

print(len(scene_graphs))
