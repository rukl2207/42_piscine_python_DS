from analytics import Research
import config


if __name__ == '__main__':
    # if len(sys.argv) != 2:
    #     raise AttributeError(f"Error: Wrong number of arguments.\n"
    #                          f"Usage: python3 {os.path.basename(__file__)} data.csv")
    research = Research(config.input_file)
    analytics = research.Analytics(research.file_reader())
    observation = analytics.counts()
    fraction = analytics.fractions(observation[0], observation[1])
    predict_random_lst = analytics.predict_random(config.num_of_steps)
    predict_counts = research.Analytics(predict_random_lst).counts()
    result = config.get_report(observation, fraction, config.num_of_steps, predict_counts)
    analytics.save_report_to_file(result, config.report_filename, config.report_file_extension)
