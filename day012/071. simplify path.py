class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        '''
        / ignore
        /.. pop the list if not empty
        /a push
        /. ignore
        how to seperate them
        '''
        x = path.split('/')
        ret = []
        for i in range(len(x)):
            if x[i] == '' or x[i] == '.':
                continue
            elif x[i] == '..' and ret != []:
                ret.pop()
            elif x[i] == '..':
                continue
            else:
                ret.append(x[i])

        y  = '/' + '/'.join(ret)
        return y
