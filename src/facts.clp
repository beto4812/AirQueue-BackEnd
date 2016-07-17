(deftemplate person
    (slot age)
    (slot sensitivity) ;low(1) ;medium(2); high (3)
    (slot asthma) ;true; false
    (slot sex)
)

(deftemplate pollutant
    (slot name)
    (slot value)
)

(deftemplate pollutionLevel
    (slot value) ;air quality index
)

(deftemplate advice
    (slot text)
    (slot level); 1; 2; 3 ;keep top level advice
)

(defrule enjoy_usual_activities_everyone_1_3
    ?pol <- (pollutionLevel {value <= 3})
    ?per <- (person)
    =>
    (retract ?per ?pol)
    (assert
        (advice (text "Enjoy your usual outdoor activities")
        (level 10)))
)

(defrule enjoy_usual_activities_general_4_6
    ?pol <- (pollutionLevel {value >= 4 && value <= 6})
    ?per <- (person {sensitivity == 1})
    =>
    (retract ?per ?pol)
    (assert
        (advice (text "Enjoy your usual outdoor activities")
        (level 11)))
)

(defrule consider_reducing_strenuous_activity_sensitive_4_6
    ?per <- (person {sensitivity >= 2})
    ?pol <- (pollutionLevel {value >= 4 && value <= 6})
    =>
    (retract ?per ?pol)
    (assert
        (advice (text "Consider reducing strenuous physical activity, particularly outdoors")
        (level 25)))
)

(defrule consider_reducing_strenuous_activity_general_7_9
    ?per <- (person {sensitivity <= 2})
    ?pol <- (pollutionLevel {value >= 7 && value <= 9} )
    =>
    (retract ?per ?pol)
    (assert
        (advice (text "If you are experiencing discomfort such as sore eyes, cough or sore throat you should consider reducing activity, particularly outdoors")
        (level 20)))
)

(defrule reduce_strenuous_activity_sensitivity_sensitive_7_9
    ?per <- (person {sensitivity == 3})
    ?pol <- (pollutionLevel {value >= 7 && value <= 9} )
    =>
    (retract ?per ?pol)
    (assert
        (advice (text "Reduce strenuous physical exertion, particularly outdoors, and particularly if you experience symptoms")
        (level 30)))
)

(defrule reduce_strenuous_activity_elder_7_9
    ?per <- (person {age >= 65})
    ?pol <- (pollutionLevel {value >= 7 && value <= 9} )
    =>
    (retract ?per ?pol)
    (assert
        (advice (text "Reduce physical exertion, particularly outdoors.")
        (level 35)))
)


(defrule reduce_strenuous_general_10
    ?per <- (person {sensitivity == 1})
    ?pol <- (pollutionLevel {value >= 10} )
    =>
    (retract ?per ?pol)
    (assert
        (advice (text "Reduce strenuous physical exertion, particularly outdoors, and particularly if you experience symptoms")
        (level 34)))
)

(defrule avoid_strenuous_sensitive_10
    ?per <- (person {sensitivity >= 2})
    ?pol <- (pollutionLevel {value >= 10} )
    =>
    (retract ?per ?pol)
    (assert
        (advice (text "Avoid strenuous physical activity.")
        (level 36)))
)

(defrule multiple_advices_1
    ?adv1 <- (advice (level ?lvl1))
    ?adv2 <- (advice (level ?lvl2))
    (test (< ?lvl1 ?lvl2))
    =>
    (retract ?lvl1)
)

(defrule multiple_advices_1
    ?adv1 <- (advice (level ?lvl1))
    ?adv2 <- (advice (level ?lvl2))
    (test (> ?lvl1 ?lvl2))
    =>
    (retract ?lvl2)
)

(defquery all-advices
  (advice))

(defquery all-person
    (person))

(defquery all-pollutionLevel
        (pollutionLevel))