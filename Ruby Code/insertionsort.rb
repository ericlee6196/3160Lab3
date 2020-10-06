def sort(array)
    for i in 1...(array.length)
        j = i
        while j > 0
            if array[j-1] > array[j]
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
            else
                break
            end
            j = j - 1
        end
    end
    return array
end

arr = Array.new
arr << '32' << '15' << '89' << '53' << '99' << '27'
sort(arr)
arr.each do |arr|
  puts arr
end