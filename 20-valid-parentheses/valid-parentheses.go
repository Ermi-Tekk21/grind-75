func isValid(s string) bool {
    stack := []string{}
    pairs := map[string]string{"(": ")", "{": "}", "[": "]"}

    for _, c := range s {
        if _, ok := pairs[string(c)]; ok {
            stack = append(stack, string(c))
        } else {
            if len(stack) == 0 || pairs[stack[len(stack)-1]] != string(c) {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }

    return len(stack) == 0 
}