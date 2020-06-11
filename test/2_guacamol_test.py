from evomol import run_model

run_model({
    "obj_function": "guacamol",
    "search_parameters": {
        "max_steps": 100,
        "pop_max_size": 1000,
        "guacamol_init_top_100": False},
    "io_parameters": {
        "model_path": "2_guacamol/"
    },
})