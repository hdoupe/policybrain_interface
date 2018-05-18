def default_data(meta_information):
    """
    Return parameter data read from JSON file.

    Parameters
    ----------
    metadata: boolean
            include extra parameter information or just the default values
    **meta_information: keyword arguments specifying required configuration
            parameters. EX: start_year, country

    Returns
    -------
    params: dictionary of data
    """
    pass

def to_json_reform(raw_web_input, **meta_information):
    """
    Read posted data and convert into desired format. The posted data is of the
    format {'parameter_name': string(value)}. This data undergoes initial
    validation by PolicyBrain to make sure it is not malicious. The current
    PolicyBrain implementation does:

    with start_year = 2017 and cls = taxcalc.Policy convert

    ```
    fields = {'_CG_nodiff': [False]},
              '_FICA_ss_trt': ["*", 0.1, "*", 0.2],
              '_ID_Charity_c_cpi': True,
              '_EITC_rt_2kids': [1.0]}
    ```

    to

    ```
    reform = {'_CG_nodiff': {'2017': [False]},
              '_FICA_ss_trt': {'2020': [0.2], '2018': [0.1]},
              '_ID_Charity_c_cpi': {'2017': True},
              '_EITC_rt_2kids': {'2017': [1.0]}}
    ```

    Parameters
    ----------
    raw_web_input: dictionary of data posted by the GUI

    **meta_information: same keywords as default_data

    Returns
    -------
    json_string: JSON specification object

    Notes
    -----
    It will be difficult to decide the hand-off here.
    Option 1: send the raw input to the model (after checking to see if
            it is malicious).
    Option 2: PolicyBrain is responsible to parsing it to close to the upstream
            project's desired data types (as done in
            PolicyBrain-param_formatters.parse_value)
    Option 2 needs to be done on the server on which this language-specific
    process is running. If it is done on the webserver, then we would either
    have to parse it into a close Python type and then serialize it before
    sending it to the cluster gateway or we would have to parse the input
    values in the cluster gateway before handing the input off to
    `to_json_reform`.

    If we decide to parse it to a close Python object type, then there are
    some interesting projects that may be able to help serialize with out
    losing information about the object's data type.
    """
    pass

def read_json_param_objects(*json_objects):
    """
    Read JSON file (as created in `to_json_reform`) and convert to to be
    validated and submitted to the run endpoint

    Returns
    -------
    param_dict: formatted dictionary
    """
    pass

def parameter_validation_messages(user_modifications):
    """
    Generate warnings and errors for parameter specifications (as created by
    `read_json_param_objects`)

    Parameters
    -----------
    user_modifications : dict created by read_json_param_objects

    Returns
    ------
    message_dict : dict with endpoint specific warning and error messages
    """
    pass

def run_endpoint_suffix(user_modifications):
    """
    An endpoint for PB to submit validated user specified parameters

    Parameters
    -----------
    user_modifications: as created in `read_json_param_objects`

    Returns
    --------
    results: dictionary of results

    Notes:
    ------
    The tricky part here is figuring out how to compress and serialize this
    data so that it can be delivered back to the user. Is this the upstream
    project's responsibility or PolicyBrain's responsibility?

    This function may be wrapped in another function that:
        - Establishes cluster and redis/message service network connection
        - Marks the job status
        - Responds to queries
        - Serializes results?
    """
    pass
