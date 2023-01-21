import logging
from analytics import Research
import config


if __name__ == '__main__':
    try:
        logging.basicConfig(filename=config.log_file, level=logging.DEBUG, format='%(asctime)s %(message)s', filemode='w')
        research = Research(config.input_file)
        analytics = research.Analytics(research.file_reader())
        observation = analytics.counts()
        fraction = analytics.fractions(observation[0], observation[1])
        predict_random_lst = analytics.predict_random(config.num_of_steps)
        predict_counts = research.Analytics(predict_random_lst).counts()
        result = config.get_report(observation, fraction, config.num_of_steps, predict_counts)
        analytics.save_report_to_file(result, config.report_filename, config.report_file_extension)
        research.send_message_to_slack(config.url_webhook, config.message_success)
    except Exception as err:
        print("Exception is raised.", err)
        research.send_message_to_slack(config.url_webhook, config.message_failure)
