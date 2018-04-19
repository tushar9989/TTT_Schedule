class QueueElement:
    storiesPerDay = 10
    def __init__(self, writer_id, remainingStoryIds, storiesPerDay):
        self.__remainingStoryIds = remainingStoryIds
        self.storiesPerDay = storiesPerDay
        self.__doneStoryIds = []
        self.__storiesToday = 0
        self.__totalDaysWaited = 0
        self.__daysWaited = 0
        self.__writer_id = writer_id

    def get_remaining_stories_count(self):
        return len(self.__remainingStoryIds)
    
    def get_story_id(self):
        if len(self.__remainingStoryIds) == 0:
            return None
        storyId = self.__remainingStoryIds.pop()
        self.__doneStoryIds.append(storyId)
        self.__storiesToday += 1
        self.__daysWaited = 0
        return storyId

    def reset_for_day_start(self):
        if self.__storiesToday == 0:
            self.__daysWaited += 1
            self.__totalDaysWaited += 1
        self.__storiesToday = 0

    def __get_days_waited_contribution(self):
        if self.__daysWaited == 0:
            return 0
        return -1 * pow(2, self.__daysWaited)

    def __get_stories_today_contribution(self):
        return int(round((self.__storiesToday / self.storiesPerDay) * 100))

    def __get_percentage_completed(self):
        return int(round(( len(self.__doneStoryIds) / ( len(self.__doneStoryIds) + len(self.__remainingStoryIds) ) ) * 100))

    def get_priority(self):
        return self.__get_percentage_completed() + self.__get_days_waited_contribution() + self.__get_stories_today_contribution()

    def get_average_wait_time(self):
        return self.__totalDaysWaited / len(self.__doneStoryIds)

    def __str__(self):
        return "Writer: " + self.__writer_id + "\nValues:\n" + str(self.__remainingStoryIds)