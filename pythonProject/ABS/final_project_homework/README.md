# Final project 

### Snake game 2D - Reinforcement Learning 

Technologies used: 
- [Pygame](https://www.pygame.org/docs/)
- [Gym](https://www.gymlibrary.dev/index.html) or [Gymnasium](https://gymnasium.farama.org/index.html)
- [StableBaselines3](https://stable-baselines3.readthedocs.io/en/master/index.html)
#####
You need the following libraries:
- ``pip install pygame``
- ``pip install shimmy``
- ``pip install tensorboard``
- ``pip install gym``
- ``pip install stable-baseline3``

Minimal requirements:
- ``OS: Windows-10-10.0.19045-SP0 10.0.19045``
- ``Python: 3.10.4``
- ``Stable-Baselines3: 2.2.1``
- ``PyTorch: 2.1.0+cpu``
- ``GPU Enabled: False``
- ``Numpy: 1.24.0``
- ``Cloudpickle: 2.2.1``
- ``Gymnasium: 0.29.1``
- ``OpenAI Gym: 0.26.2``

### Presentation & Research Paper
My [Research Paper]().
</br>
My [Presentation]().

### How To Run
First of all, in order to run this snake game 2D with
reinforcement learning, you need to navigate to ``main.py`` 
in the ``final_project_homework`` package. Then, 
in the 43th line there are several intervals that I have chosen. It's
up to you whether you want to use several intervals in order to
train the snake model or not; below that line you have other (smaller ones),
intervals, use them if you want.
Below 46th line choose what algorithm you want to use
in order to train the snake model e.g. you may want
``train_and_save_ppo_model(env, model, A2C_path, save_intervals)``
and after training, when the process will be finished, comment the 
training function and uncomment the testing function based
on what algorithm you have used in order to train the model.
In this case, the ``test_ppo_model(env, PPO_path, save_intervals[-1])``
will be used.

In the ``Traning`` folder will be saved the Logs & Saved models.

**Note**: When you only want to test already trained models from
the ``Saved models`` package, after the testing process it will be
created another log file in the ``Logs`` package.

### External Links that helped me in the process of development in the RL

- Helpful Links & Tutorials [here](https://github.com/AceGjorgjievski/PythonProjects/blob/master/pythonProject/ABS/final_project_homework/help_links).
- Errors that I have encountered [here](https://github.com/AceGjorgjievski/PythonProjects/blob/master/pythonProject/ABS/final_project_homework/handled_erros.txt).

