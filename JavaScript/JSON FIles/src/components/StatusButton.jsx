import PropTypes from 'prop-types'

export const StatusButton = ({ text, color }) => {
  return (
    <button style={{ background: color, color: 'white'}}>
        {text}
    </button>
  )
}

StatusButton.defaultProps = {
    text: 'Status',
    color: 'green'
}

StatusButton.propTypes = {
    text: PropTypes.string.isRequired,
    color: PropTypes.string
}
