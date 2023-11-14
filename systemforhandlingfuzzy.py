class FzSets:

    def __init__(self, A=None, nA=None, B=None, nB=None):
        """
        Initializes FzSets class with two sets A and B.

        Args:
        - A (dict): First set.
        - nA (str): Name of the first set.
        - B (dict): Second set.
        - nB (str): Name of the second set.
        """
        self.A = A or dict()
        self.B = B or dict()
        self.Aname = nA
        self.Bname = nB

        self.complement_A = dict()
        self.complement_B = dict()
        self.union_AB = dict()
        self.intersection_AB = dict()
        self.differenceAB = dict()
        self.differenceBA = dict()

        self.change_union = False
        self.change_intersection = False
        self.change_complement = False

    def union_op(self):
        """
        Performs union operation on sets A and B and prints the result.
        """
        if not self.change_union:
            sa = set(self.A.keys())
            sb = set(self.B.keys())
            intersection_set = sa.intersection(sb)

            for i in intersection_set:
                self.union_AB[i] = max(self.A[i], self.B[i])
            for i in sa - intersection_set:
                self.union_AB[i] = self.A[i]
            for i in sb - intersection_set:
                self.union_AB[i] = self.B[i]

            print('Result of UNION operation:', self.union_AB)
        else:
            print('Result of UNION operation:', self.union_AB)

    def intersection_op(self):
        """
        Performs intersection operation on sets A and B and prints the result.
        """
        if not self.change_intersection:
            sa = set(self.A.keys())
            sb = set(self.B.keys())
            intersection_set = sa.intersection(sb)

            for i in intersection_set:
                self.intersection_AB[i] = min(self.A[i], self.B[i])
            for i in sa - intersection_set:
                self.intersection_AB[i] = 0.0
            for i in sb - intersection_set:
                self.intersection_AB[i] = 0.0

            print('Result of INTERSECTION operation:\n\t\t', self.intersection_AB)
            self.change_intersection = True
        else:
            print('Result of INTERSECTION operation:\n\t\t', self.intersection_AB)

    def complement_op(self):
        """
        Performs complement operation on sets A and B and prints the result.
        """
        if not self.change_complement:
            for i in self.A:
                self.complement_A[i] = 1 - self.A[i]
            for i in self.B:
                self.complement_B[i] = 1 - self.B[i]

            print('Result of COMPLEMENT on', self.Aname, 'operation:', self.complement_A)
            print('Result of COMPLEMENT on', self.Bname, 'operation:', self.complement_B)

            self.change_complement = True
        else:
            print('Result of COMPLEMENT on', self.Aname, 'operation:', self.complement_A)
            print('Result of COMPLEMENT on', self.Bname, 'operation:', self.complement_B)

    def __one_minus_two(self, L, R):
        """
        Helper method for calculating the difference of two sets.

        Args:
        - L (dict): First set.
        - R (dict): Second set.

        Returns:
        - dict: Resulting set of L - R.
        """
        minus_d = dict()
        Rcomp = {i: 1 - R[i] for i in R}
        sa = set(L.keys())
        sb = set(R.keys())
        intersection_set = sa.intersection(sb)

        for i in intersection_set:
            minus_d[i] = min(L[i], Rcomp[i])
        for i in sa - intersection_set:
            minus_d[i] = 0.0
        for i in sb - intersection_set:
            minus_d[i] = 0.0

        return minus_d

    def A_minus_B(self):
        """
        Performs A - B operation and prints the result.
        """
        self.differenceAB = self.__one_minus_two(self.A, self.B)
        print('Result of DIFFERENCE', self.Aname, '|', self.Bname, 'operation:\n\t\t', self.differenceAB)

    def B_minus_A(self):
        """
        Performs B - A operation and prints the result.
        """
        self.differenceBA = self.__one_minus_two(self.B, self.A)
        print('Result of DIFFERENCE', self.Bname, '|', self.Aname, 'operation:\n\t\t', self.differenceBA)

    def change_sets(self, A, B):
        """
        Changes the sets A and B and resets the cache.

        Args:
        - A (dict): New first set.
        - B (dict): New second set.
        """
        self.A = A
        self.B = B

        print('\nSet', self.Aname, ':', self.A)
        print('Set', self.Bname, ':', self.B, end='')

        self.change_union = True
        self.change_intersection = True
        self.change_complement = True
        print('\t\t\t Cache Reset')

    def display_sets(self):
        """
        Displays the current sets A and B.
        """
        print('\nSet', self.Aname, ':', self.A)
        print('Set', self.Bname, ':', self.B)
