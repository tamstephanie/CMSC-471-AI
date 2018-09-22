;; There is only one block, A, which is on the table.  A can with red
;; paint is on the table.  There is a clean brush on the table.  Our
;; goal is to have A be red, and the arm empty.

(define (problem 1)
  (:domain hw5)
  (:objects A brush can)
  (:init (arm-empty)
  	 (block A)
	 (on-table A)
	 (clear A)

	 (brush brush)
	 (on-table brush)
	 (clear brush)
	 (clean brush)

	 (paint-can can red)
	 (on-table can)
	 (clear can))
  (:goal (and (arm-empty) 
    	 (color A red))))


