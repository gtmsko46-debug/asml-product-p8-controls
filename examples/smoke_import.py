from asml_product_p8_controls import recover_from_glitch
print(recover_from_glitch({"n_tools": 4, "glitch_severity": 0.25}).to_dict())
