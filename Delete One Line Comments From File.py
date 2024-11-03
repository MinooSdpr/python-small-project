def remove_comments_from_file(path, comment_char, target_path):
 """Removes comments from a file, writing the result to a new file.

 This function takes a file path, a comment character, and a target path as input.
 It reads the file line by line, removing any text after the specified
 comment character on each line. The resulting lines are written to a new file
 at the specified target path.

 Args:
  path: The path to the file containing comments to be removed.
  comment_char: The character that marks the beginning of a comment.
  target_path: The path to the new file where the results will be written.

 Returns:
  None. The function writes the modified file to the target path.
 """
 file = open(path, 'r')
 new_file = open(target_path, 'w')

 lines = file.readlines()
 for line in lines:
  index_sharp = line.find(comment_char)
  if index_sharp != -1:
   new_file.write(line[:index_sharp])
  else:
   new_file.write(line)
  new_file.write('\n')
 file.close()
 new_file.close()

path = input('Enter file path: ')
comment_char = input('Enter comment character symbol: ')
remove_comments_from_file(path, comment_char, 'target.txt')
