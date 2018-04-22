import math
class QueueElement:
    def __init__(self, writer_id, remainingStoryIds, storiesPerDay, timeImportance):
        self.__remainingStoryIds = remainingStoryIds
        self.storiesPerDay = storiesPerDay
        self.__timeImportance = timeImportance
        self.__doneStoryIds = []
        self.__storiesToday = 0
        self.__totalDaysWaited = 0
        self.__daysWaited = 0
        self.writer_id = writer_id

    def get_remaining_stories_count(self):
        return len(self.__remainingStoryIds)

    def get_done_stories_count(self):
        return len(self.__doneStoryIds)

    def get_total_stories_count(self):
        return self.get_done_stories_count() + self.get_remaining_stories_count()
    
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
        return -1 * int(pow(1.585, self.__daysWaited) * self.__timeImportance)

    def __get_stories_today_contribution(self):
        return int(round((float(self.__storiesToday) / self.storiesPerDay) * 100))

    def get_percentage_completed(self):
        return int(round(( float(len(self.__doneStoryIds)) / ( len(self.__doneStoryIds) + len(self.__remainingStoryIds) ) ) * 100))

    def get_priority(self):
        return self.get_percentage_completed() + self.__get_days_waited_contribution() + self.__get_stories_today_contribution()

    def get_average_wait_time(self):
        return 0 if len(self.__doneStoryIds) == 0 else float(self.__totalDaysWaited) / len(self.__doneStoryIds)

    def __str__(self):
        return "\nW: " + self.writer_id + "\nP: " + str(self.get_priority()) + "\nD: " + str(self.get_done_stories_count()) + " R: " + str(self.get_remaining_stories_count()) + ", P: " + str(self.get_percentage_completed()) + "%\nW: " + str(self.get_average_wait_time())
