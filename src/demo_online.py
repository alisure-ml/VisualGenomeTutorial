import api as vg_api

# 1. 获取所有的图片ID
# ids = vg_api.get_all_image_ids()
# print(ids)


# 2. 获取某个范围的ID
# ids = vg_api.get_image_ids_in_range(start_index=1000, end_index=1300)
# print(ids)


# 3. 获取图片数据
# image = vg_api.get_image_data()
# print(image)


# 4. 获取图片的区域描述
# Region Graphs are tiny scene graphs for a particular region of an image.
# It contains: objects, attributes and relationships.
# Objects are localized in the image with bounding boxes.
# Attributes modify the object while Relationships are interactions between pairs of objects.
# region = vg_api.get_region_descriptions_of_image()
# print(region)


# 5. 获取图片的场景图：对象区域、对象的属性、对象之间的关系
# Each scene graph has three components: objects, attributes and relationships.
# Objects are localized in the image with bounding boxes.
# Attributes modify the object while Relationships are interactions between pairs of objects.
# scene = vg_api.get_scene_graph_of_image()
# print(scene)


# 6. 获取图片的问答对
# Each Question Answer object contains the id of the question-answer pair, the id of image, the question and the answer
# string, as well as the list of question objects and answer objects identified and canonicalized in the qa pair.
# qa = vg_api.get_QA_of_image()
# print(qa)


# 7. 获取指定数量的问答对
# qas = vg_api.get_all_QAs(qtotal=100)
# print(qas)


# 8. 获取指定类型的问答对
# To query for a particular type of question, set qtype to what, who, why, where, when, how.
# qas_type = vg_api.get_QA_of_type(qtype="what", qtotal=100)
# print(qas_type)
