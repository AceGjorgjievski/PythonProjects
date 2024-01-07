

def state_to_key(state):
    # Check if the state is a tuple, and if so, return the first element
    if isinstance(state, tuple):
        return state[0]
    # If it's a single integer, return the state as is
    elif isinstance(state, int):
        return state
    # Handle any other cases here, like returning a default key
    else:
        return "unknown_state_key"
