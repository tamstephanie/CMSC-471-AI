;; Three blocks (A B and C) are on the table along with three sprayers
;; (red, green, blue), three paint cans (red, green, blue), a water
;; bucket and a clean brush.  Paint A, B and C red, blue and green,
;; respectively. End with the arm empty and the brush clean.

(define (problem 3)
  (:domain hw5)
  (:objects A B C sprayR sprayG sprayB canR canG canB bucket brush)
  (:init (arm-empty)
  	 (block A)
	 (on-table A)
	 (clear A)

	 (block B)
	 (on-table B)
	 (clear B)

	 (block C)
	 (on-table C)
	 (clear C)

	 (sprayer sprayR red)
	 (on-table sprayR)
	 (clear sprayR)

         (sprayer sprayG green)
         (on-table sprayG)
	 (clear sprayG)

         (sprayer sprayB blue)
         (on-table sprayB)
	 (clear sprayB)

	 (paint-can canR red)
	 (on-table canR)
	 (clear canR)

         (paint-can canG green)
         (on-table canG)
	 (clear canG)

         (paint-can canB blue)
         (on-table canB)
	 (clear canB)

	 (water-bucket bucket)
	 (on-table bucket)
	 (clear bucket)
	 
	 (brush brush)
	 (on-table brush)
	 (clear brush)
	 (clean brush))
  (:goal (and (arm-empty)
  	 (color A red)
	 (color B blue)
	 (color C green)
	 (clean brush))))





