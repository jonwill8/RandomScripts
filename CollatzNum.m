classdef CollatzNum
    properties
        num
        collatz_count
    end
    methods
        function obj = CollatzNum(val) %constructor
            if nargin == 1
                obj.num = val;
                obj.collatz_count = calc_collatz_length(val);
            end
        end
        function len = getLen(obj)
            len = obj.collatz_count;
        end
    end
end