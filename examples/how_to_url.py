from pywikihow import HowTo

how_to = HowTo("https://www.wikihow.com/Train-a-Dog")

data = how_to.as_dict()

print(how_to.url)
print(how_to.title)
print(how_to.n_steps)
print(how_to.summary)

first_step = how_to.steps[0]
first_step.print()
data = first_step.as_dict()

how_to.print(extended=True)