import React, { useState, useCallback } from 'react';
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  StyleSheet,
  SafeAreaView,
} from 'react-native';
import { StatusBar } from 'expo-status-bar';
import { evaluate } from 'mathjs';

const ROWS = [
  ['AC', 'C', '/', '*'],
  ['7', '8', '9', '-'],
  ['4', '5', '6', '+'],
  ['1', '2', '3', '='],
  ['0', '.'],
];

const OPERATORS = ['/', '*', '-', '+', '='];
const CLEAR_BUTTONS = ['AC', 'C'];

const formatResult = (value) => {
  if (!isFinite(value)) return 'Error';
  if (Number.isInteger(value)) return String(value);
  return String(parseFloat(value.toFixed(10)));
};

export default function App() {
  const [expression, setExpression] = useState('');
  const [result, setResult] = useState('0');
  const [justEvaluated, setJustEvaluated] = useState(false);

  const handlePress = useCallback(
    (label) => {
      console.log(label);

      if (label === 'AC') {
        setExpression('');
        setResult('0');
        setJustEvaluated(false);
        return;
      }

      if (label === 'C') {
        if (expression.length === 0) return;
        setExpression((prev) => {
          const updated = prev.slice(0, -1);
          if (updated === '') setResult('0');
          return updated;
        });
        setJustEvaluated(false);
        return;
      }

      if (label === '=') {
        const expr = expression.trim() || '0';
        try {
          const value = evaluate(expr);
          setResult(formatResult(value));
        } catch (e) {
          console.log('Evaluation error:', e.message);
          setResult('Error');
        }
        setJustEvaluated(true);
        return;
      }

      if (OPERATORS.includes(label)) {
        if (justEvaluated) {
          setExpression(
            result !== 'Error' ? result + label : label === '-' ? '-' : label
          );
          setJustEvaluated(false);
          return;
        }
        if (expression === '' && label !== '-') return;
        const last = expression.slice(-1);
        if (OPERATORS.includes(last)) {
          if (label === '-') {
            setExpression((prev) => prev + '-');
          } else {
            setExpression((prev) => prev.slice(0, -1) + label);
          }
        } else {
          setExpression((prev) => prev + label);
        }
        setJustEvaluated(false);
        return;
      }

      if (justEvaluated) {
        setExpression(label === '.' ? '0.' : label);
        setResult('0');
        setJustEvaluated(false);
        return;
      }

      if (label === '.') {
        const parts = expression.split(/[+\-*/]/);
        const currentSegment = parts[parts.length - 1];
        if (currentSegment.includes('.')) return;
        if (currentSegment === '') {
          setExpression((prev) => prev + '0.');
          return;
        }
      }

      setExpression((prev) => prev + label);
    },
    [expression, result, justEvaluated]
  );

  const displayExpression = expression === '' ? '0' : expression;

  const getButtonStyle = (label) => {
    if (OPERATORS.includes(label))
      return [styles.button, styles.operatorButton];
    if (CLEAR_BUTTONS.includes(label))
      return [styles.button, styles.clearButton];
    return styles.button;
  };

  const getButtonTextStyle = (label) => {
    if (OPERATORS.includes(label))
      return [styles.buttonText, styles.operatorButtonText];
    if (CLEAR_BUTTONS.includes(label))
      return [styles.buttonText, styles.clearButtonText];
    return styles.buttonText;
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <View style={styles.container}>
        <View style={styles.header}>
          <Text style={styles.headerTitle}>Calculator</Text>
        </View>

        <View style={styles.displayContainer}>
          <TextInput
            style={styles.expressionInput}
            value={displayExpression}
            editable={false}
            pointerEvents="none"
          />
          <TextInput
            style={styles.resultInput}
            value={result}
            editable={false}
            pointerEvents="none"
          />
        </View>

        <View style={styles.grid}>
          {ROWS.map((row, rowIndex) => (
            <View key={rowIndex} style={styles.row}>
              {row.map((label) => (
                <TouchableOpacity
                  key={label}
                  style={getButtonStyle(label)}
                  onPress={() => handlePress(label)}
                  activeOpacity={0.7}
                >
                  <Text style={getButtonTextStyle(label)}>{label}</Text>
                </TouchableOpacity>
              ))}
            </View>
          ))}
        </View>
      </View>
      <StatusBar style="light" />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: '#1C1C1E',
  },
  container: {
    flex: 1,
  },
  header: {
    paddingVertical: 16,
    alignItems: 'center',
    borderBottomWidth: 1,
    borderBottomColor: '#3A3A3C',
    backgroundColor: '#2C2C2E',
  },
  headerTitle: {
    fontSize: 20,
    fontWeight: '700',
    color: '#FFFFFF',
  },
  displayContainer: {
    padding: 20,
    backgroundColor: '#1C1C1E',
  },
  expressionInput: {
    fontSize: 18,
    color: '#8E8E93',
    textAlign: 'right',
    paddingVertical: 8,
  },
  resultInput: {
    fontSize: 32,
    color: '#FFFFFF',
    textAlign: 'right',
    fontWeight: '300',
    paddingVertical: 8,
  },
  grid: {
    flex: 1,
    padding: 10,
    justifyContent: 'flex-end',
  },
  row: {
    flexDirection: 'row',
    marginBottom: 10,
  },
  button: {
    flex: 1,
    marginHorizontal: 5,
    height: 70,
    borderRadius: 35,
    backgroundColor: '#2C2C2E',
    justifyContent: 'center',
    alignItems: 'center',
  },
  operatorButton: {
    backgroundColor: '#FF9F0A',
  },
  clearButton: {
    backgroundColor: '#3A3A3C',
  },
  buttonText: {
    fontSize: 24,
    color: '#FFFFFF',
    fontWeight: '400',
  },
  operatorButtonText: {
    color: '#FFFFFF',
    fontWeight: '600',
  },
  clearButtonText: {
    color: '#FF453A',
  },
});
