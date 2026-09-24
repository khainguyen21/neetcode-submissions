class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet <Integer> checkUp = new HashSet<Integer>(); 

        for (int num: nums)
        {
            if (checkUp.contains(num))
            {
                return true; 
            }
            else 
            {
                checkUp.add(num);
            }
        }
        
        return false; 
        
    }
}

