# the external parameters

input_file = '../ex00/data.csv'
num_of_steps = 3
report_filename = 'report'
report_file_extension = 'txt'


def get_report(observation, fraction, steps, predict_counts) -> str:
	return (
		f"Report\nWe have made {sum(observation)} observations from tossing a coin: "
		f"{observation[0]} of them were tails and {observation[1]} of them were heads. "
		f"The probabilities are {fraction[0]:.2f}% and {fraction[1]:.2f}%, respectively. "
		f"Our forecast is that in the next {steps} observations we will have: {predict_counts[0]} "
		f"tail and {predict_counts[1]} heads.")
