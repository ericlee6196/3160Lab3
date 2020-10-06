def sort(arr)
  return arr if arr.size <= 1 
  loop do
    swapped = false
    0.upto(arr.size-2) do |i|
      if arr[i] > arr[i+1]
        arr[i], arr[i+1] = arr[i+1], arr[i] 
        swapped = true
      end
    end
    break unless swapped
  end
  arr
end

arr = Array.new
arr << '15' << '12' << '13' << '53' << '34'
sort(arr)
arr.each do |arr|
  puts arr
end