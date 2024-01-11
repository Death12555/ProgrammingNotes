class Solution:
    def isValid(self, s: str) -> bool:
        valid_paranthesis= {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        def custom_pop(my_list):
            if len(my_list)==0:
                print("Cannot pop from an empty list.")
                return None
    
            popped_element= my_list[-1]
            my_list= my_list[:-1]
    
            return popped_element, my_list
            
        paranthesis= []

        for char in s:
            if char in valid_paranthesis:
                paranthesis.append(char)
            else:
                if not paranthesis or char!= valid_paranthesis[paranthesis.pop()]:
                    return False
        return not paranthesis