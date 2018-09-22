;; Block A is on the table, B is on A and C on B.  On the table are a
;; water bucket, a red sprayer, cans of blue and green paint and a
;; clean brush.  The goal is to make A red, B green and C blue and to
;; have A on B, B on C and C on the table and the brush clean and arm
;; empty.

(define (problem 4)
  (:domain hw5)
  (:objects A B C bucket sprayR canB canG brush)
  (:init (arm-empty)
  	 (block A)
	 (on-table A)

	 (block B)
	 (on B A)

	 (block C)
	 (clear C)
	 (on C B)

	 (water-bucket bucket)
	 (on-table bucket)
	 (clear bucket)	 

	 (sprayer sprayR red)
	 (on-table sprayR)
	 (clear sprayR)

	 (paint-can canB blue)
	 (on-table canB)
	 (clear canB)

	 (paint-can canG green)
	 (on-table canG)
	 (clear canG)

	 (brush brush)
	 (on-table brush)
	 (clear brush)
	 (clean brush))
  (:goal (and (arm-empty)
  	 (color A red)
	 (color B green)
	 (color C blue)
	 (on A B)
	 (on B C)
	 (on-table C)
	 (clean brush))))


