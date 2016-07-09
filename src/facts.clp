(deftemplate person
    (slot age)
    (slot sensitivity)
    (slot sex)
)


(deftemplate pollutant
    (slot name)
    (slot value)
)

(deftemplate pollutionLevel
    ;
    (slot value)
)

(deftemplate advice
    (slot advice-text)
)




(defrule recommend_outdoor_activities
    ?p <- (person (age ?x))
    (test (< ?x 30))
    =>
    (printout t ?p" is young " crlf)
)

defrule

(assert (person (age 20) (sensitivity high) (sex male)))