;; Block A is on the table, block B on A and there is nothing on B.  A
;; water bucket, a brush, a A blue sprayer and a red paint can are on
;; the table and clear.  The goal is to for A to be colored red and B
;; blue and the brush be clean.

(define (problem 2)
  (:domain hw5)
  (:objects A B sprayB can brush bucket)
  (:init (arm-empty)
  	 (block A)
	 (on-table A)

	 (block B)
	 (clear B)
	 (on B A)
	 
	 (sprayer sprayB blue)
	 (on-table sprayB)
	 (clear sprayB)
	 
	 (brush brush)
	 (on-table brush)
	 (clear brush)
	 (clean brush)

	 (paint-can can red)
	 (on-table can)
	 (clear can)

	 (water-bucket bucket)
	 (on-table bucket)
	 (clear bucket))
  (:goal (and (arm-empty)
  	 (color A red)
	 (color B blue)
	 (clean brush))))
