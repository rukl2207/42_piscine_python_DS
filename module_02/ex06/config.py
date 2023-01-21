# the external parameters

input_file = '../ex00/data.csv'
num_of_steps = 3
report_filename = 'report'
report_file_extension = 'txt'
log_file = "analytics.log"
url_webhook = "https://hooks.slack.com/services/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"
message_success = {"text": "The report has been successfully created"}
message_failure = {"text": "The report hasn’t been created due to an error"}


def get_report(observation, fraction, steps, predict_counts) -> str:
	return (
		f"Report\nWe have made {sum(observation)} observations from tossing a coin: "
		f"{observation[0]} of them were tails and {observation[1]} of them were heads. "
		f"The probabilities are {fraction[0]:.2f}% and {fraction[1]:.2f}%, respectively. "
		f"Our forecast is that in the next {steps} observations we will have: {predict_counts[0]} "
		f"tail and {predict_counts[1]} heads.")
