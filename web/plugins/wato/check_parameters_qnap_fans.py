group = "checkparams"                                                                                                                                                                                                                        
subgroup_applications = _("Temperature, Humidity, Electrical Parameters, etc.")
register_check_parameters(
    subgroup_applications,
    "qnap_fans",
    _("Parameters for QNAP Fans"),
    Dictionary(
        elements = [
            ('levels', Tuple(
                title = _('FanSpeed Thresholds'),
                help = _("Set FanSpeed Thresholds for alarms"),
                elements = [
                    Integer(title = _("Warning at"), unit = _("RPM"), default_value = 6000),
                    Integer(title = _("Critical at"), unit = _("RPM"), default_value = 6500),
                ])),
        ],
    ),
    TextAscii(
        title = _("Name of service"),
        allow_empty = False,
    ),
    'dict',
)
