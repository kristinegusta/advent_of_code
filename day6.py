from puzzle_inputs.signal import signal

def check_unique(str):
  for i in range(len(str)):
    for j in range(i + 1,len(str)):
      if(str[i] == str[j]):
        return False
  return True

# For part 1 the end position is 3 ( unique characters needed for the puzzle - 1 )
end_position = 13

while end_position < len(signal):
    start_position = end_position - 13
    substring_to_check = signal[start_position:end_position+1]
    if (check_unique(substring_to_check) and end_position > 13):
        print("Found! " + str(end_position + 1))
        break
    else:
        end_position += 1
   
        
