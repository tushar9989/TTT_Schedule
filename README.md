# TTT Scheduling

## Metrics Involved

For each writer

- Percentage of total stories published. (Maximize)
- Days waited. (Minimize)
- Stories published on the same day. (Minimize)

## Writer Happiness

There are some observations we can make.

- As the number of published stories increases the writer's happiness increases and their priority decreases. There should be a liner relationship between stories published and it's negative contribution to priority.

- As the time waited between published stories increases the writer's happiness decreases. There should be an exponential relationship between days waited and it's contribution to priority.

- Time waited should be more important to writers with high volume compared to the total number of stories we have. Hence the contribution of time waited should be proportional to the writer's volume.

- The number of times a writer is picked in a day should increase their happiness temporarily and have a negative contribution to the writer's priority.

## Overall Happiness

The overall happiness should be linearly proportional to the average published percent.

## Priority

> Lower values indicate higher priority

It is defined as **Published Stories Contribution** - **Time Waited Contribution** + **Stories Today Contribution**

### Published Stories Contribution

This is simply the percentage of stories published. Can range between 0 and 100.

### Time Waited Importance

This is the percentile of the number of stories for that writer. Ranges between 0 and 1.

### Time Waited Contribution

It is (1.585 ^ Days Waited) * Time Waited Importance.
1.585 was chosen as the base since for most of the expected values of Days Waited i.e 0 - 10 it ranges between 0 - 100.

### Stories Today Contribution

It is (Stories Today / Total Stories Each Day) * 100. It can range between 0 and 100.

## Solution Approach

- I have used a min priority queue to implement the scheduling.

- We start by grouping the stories by writer_id.

- All the writers are added to the queue and initially their priority will be 0.

- Whenever we pick a writer from the queue their days waited is reset to 0 and stories published today is incremented.

- We then pick a story from the writer's remaining stories and publish that.

- After publishing the story if the writer still has stories remaining the writer is added back to the queue.

- At the end of each day all the writers that have not had any stories published that day have their days waited incremented. Stories today is reset to 0 for writers that have had their stories published.

- The queue is then reinitialized with the updated writer objects and sorted by priority.

## How does your algorithm work towards minimizing unhappiness and also maximizing overall happiness at the same time?

It works to increase overall happiness by prioritizing writers that have had fewer stories published.

It works to decrease individual unhappiness by making sure that writers don't have to wait too long compared to their volume to get published.