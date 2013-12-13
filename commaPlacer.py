#Places commas onto big numbers
def comma(number):
    if number < 1000:
        return 'Number doesn\'t need commas'
    number = str(int(number))
    holder = []
    number = number[::-1]
    iterator = 0
    for i in number:
        iterator += 1
        holder.append(i)
        if not iterator%3 and not(i is number[-1]):
            holder.append(',')
    return ''.join(holder[::-1])