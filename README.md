# VMPlacement
A Heuristic &amp; Genetic Approach to Virtual Machine Placement

## Hueristic Approach
This approach uses takes the VM that has the minimum makeSpan and tries to place the task into them. <br>
If there is a placement problem (not enough runtime, not enough power) through all of the VMs, It will reject the task.

## Genetic Approach
This approach goes through a certain number of generations and uses Mutation, CrossOver and a Calculated Score of MakeSpan and NRT (Number of Rejected Tasks) to Improve every generation. <br>
You can see an average of MakeSpan and NRT throughout the Generations.
